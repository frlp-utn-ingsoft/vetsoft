import os

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from playwright.sync_api import sync_playwright, expect, Browser

from django.urls import reverse

from app.models import Client, Pet

import datetime

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
playwright = sync_playwright().start()
headless = os.environ.get("HEADLESS", 1) == 1
slow_mo = os.environ.get("SLOW_MO", 0)


class PlaywrightTestCase(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.browser: Browser = playwright.chromium.launch(
            headless=headless, slow_mo=int(slow_mo)
        )

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.browser.close()

    def setUp(self):
        super().setUp()
        self.page = self.browser.new_page()

    def tearDown(self):
        super().tearDown()
        self.page.close()


class HomeTestCase(PlaywrightTestCase):
    def test_should_have_navbar_with_links(self):
        self.page.goto(self.live_server_url)

        navbar_home_link = self.page.get_by_test_id("navbar-Home")

        expect(navbar_home_link).to_be_visible()
        expect(navbar_home_link).to_have_text("Home")
        expect(navbar_home_link).to_have_attribute("href", reverse("home"))

        navbar_clients_link = self.page.get_by_test_id("navbar-Clientes")

        expect(navbar_clients_link).to_be_visible()
        expect(navbar_clients_link).to_have_text("Clientes")
        expect(navbar_clients_link).to_have_attribute("href", reverse("clients_repo"))

    def test_should_have_home_cards_with_links(self): 
        self.page.goto(self.live_server_url)

        home_clients_link = self.page.get_by_test_id("home-Clientes")

        expect(home_clients_link).to_be_visible()
        expect(home_clients_link).to_have_text("Clientes")
        expect(home_clients_link).to_have_attribute("href", reverse("clients_repo"))


class ClientsRepoTestCase(PlaywrightTestCase):
    def test_should_show_message_if_table_is_empty(self):
        self.page.goto(f"{self.live_server_url}{reverse('clients_repo')}")

        expect(self.page.get_by_text("No existen clientes")).to_be_visible()

    def test_should_show_clients_data(self):
        Client.objects.create(
            name="Juan Sebastián Veron",
            address="13 y 44",
            phone="221555232",
            email="brujita75@hotmail.com",
        )

        Client.objects.create(
            name="Guido Carrillo",
            address="1 y 57",
            phone="221232555",
            email="goleador@gmail.com",
        )

        self.page.goto(f"{self.live_server_url}{reverse('clients_repo')}")

        expect(self.page.get_by_text("No existen clientes")).not_to_be_visible()

        expect(self.page.get_by_text("Juan Sebastián Veron")).to_be_visible()
        expect(self.page.get_by_text("13 y 44")).to_be_visible()
        expect(self.page.get_by_text("221555232")).to_be_visible()
        expect(self.page.get_by_text("brujita75@hotmail.com")).to_be_visible()

        expect(self.page.get_by_text("Guido Carrillo")).to_be_visible()
        expect(self.page.get_by_text("1 y 57")).to_be_visible()
        expect(self.page.get_by_text("221232555")).to_be_visible()
        expect(self.page.get_by_text("goleador@gmail.com")).to_be_visible()

    def test_should_show_add_client_action(self):
        self.page.goto(f"{self.live_server_url}{reverse('clients_repo')}")

        add_client_action = self.page.get_by_role(
            "link", name="Nuevo cliente", exact=False
        )
        expect(add_client_action).to_have_attribute("href", reverse("clients_form"))

    def test_should_show_client_edit_action(self):
        client = Client.objects.create(
            name="Juan Sebastián Veron",
            address="13 y 44",
            phone="221555232",
            email="brujita75@hotmail.com",
        )

        self.page.goto(f"{self.live_server_url}{reverse('clients_repo')}")

        edit_action = self.page.get_by_role("link", name="Editar")
        expect(edit_action).to_have_attribute(
            "href", reverse("clients_edit", kwargs={"id": client.id})
        )

    def test_should_show_client_delete_action(self):
        client = Client.objects.create(
            name="Juan Sebastián Veron",
            address="13 y 44",
            phone="221555232",
            email="brujita75@hotmail.com",
        )

        self.page.goto(f"{self.live_server_url}{reverse('clients_repo')}")

        edit_form = self.page.get_by_role(
            "form", name="Formulario de eliminación de cliente"
        )
        client_id_input = edit_form.locator("input[name=client_id]")

        expect(edit_form).to_be_visible()
        expect(edit_form).to_have_attribute("action", reverse("clients_delete"))
        expect(client_id_input).not_to_be_visible()
        expect(client_id_input).to_have_value(str(client.id))
        expect(edit_form.get_by_role("button", name="Eliminar")).to_be_visible()

    def test_should_can_be_able_to_delete_a_client(self):
        Client.objects.create(
            name="Juan Sebastián Veron",
            address="13 y 44",
            phone="221555232",
            email="brujita75@hotmail.com",
        )

        self.page.goto(f"{self.live_server_url}{reverse('clients_repo')}")

        expect(self.page.get_by_text("Juan Sebastián Veron")).to_be_visible()

        def is_delete_response(response):
            return response.url.find(reverse("clients_delete"))

        # verificamos que el envio del formulario fue exitoso
        with self.page.expect_response(is_delete_response) as response_info:
            self.page.get_by_role("button", name="Eliminar").click()

        response = response_info.value
        self.assertTrue(response.status < 400)

        expect(self.page.get_by_text("Juan Sebastián Veron")).not_to_be_visible()


class ClientCreateEditTestCase(PlaywrightTestCase):
    def test_should_be_able_to_create_a_new_client(self):
        self.page.goto(f"{self.live_server_url}{reverse('clients_form')}")

        expect(self.page.get_by_role("form")).to_be_visible()

        self.page.get_by_label("Nombre").fill("Juan Sebastián Veron")
        self.page.get_by_label("Teléfono").fill("221555232")
        self.page.get_by_label("Email").fill("brujita75@hotmail.com")
        self.page.get_by_label("Dirección").fill("13 y 44")

        self.page.get_by_role("button", name="Guardar").click()

        expect(self.page.get_by_text("Juan Sebastián Veron")).to_be_visible()
        expect(self.page.get_by_text("221555232")).to_be_visible()
        expect(self.page.get_by_text("brujita75@hotmail.com")).to_be_visible()
        expect(self.page.get_by_text("13 y 44")).to_be_visible()

    def test_should_view_errors_if_form_is_invalid(self):
        self.page.goto(f"{self.live_server_url}{reverse('clients_form')}")

        expect(self.page.get_by_role("form")).to_be_visible()

        self.page.get_by_role("button", name="Guardar").click()

        expect(self.page.get_by_text("Por favor ingrese un nombre")).to_be_visible()
        expect(self.page.get_by_text("Por favor ingrese un teléfono")).to_be_visible()
        expect(self.page.get_by_text("Por favor ingrese un email")).to_be_visible()

        self.page.get_by_label("Nombre").fill("Juan Sebastián Veron")
        self.page.get_by_label("Teléfono").fill("221555232")
        self.page.get_by_label("Email").fill("brujita75")
        self.page.get_by_label("Dirección").fill("13 y 44")

        self.page.get_by_role("button", name="Guardar").click()

        expect(self.page.get_by_text("Por favor ingrese un nombre")).not_to_be_visible()
        expect(
            self.page.get_by_text("Por favor ingrese un teléfono")
        ).not_to_be_visible()

        expect(
            self.page.get_by_text("Por favor ingrese un email valido")
        ).to_be_visible()

    def test_should_be_able_to_edit_a_client(self):
        client = Client.objects.create(
            name="Juan Sebastián Veron",
            address="13 y 44",
            phone="221555232",
            email="brujita75@hotmail.com",
        )

        path = reverse("clients_edit", kwargs={"id": client.id})
        self.page.goto(f"{self.live_server_url}{path}")

        self.page.get_by_label("Nombre").fill("Guido Carrillo")
        self.page.get_by_label("Teléfono").fill("221232555")
        self.page.get_by_label("Email").fill("goleador@gmail.com")
        self.page.get_by_label("Dirección").fill("1 y 57")

        self.page.get_by_role("button", name="Guardar").click()

        expect(self.page.get_by_text("Juan Sebastián Veron")).not_to_be_visible()
        expect(self.page.get_by_text("13 y 44")).not_to_be_visible()
        expect(self.page.get_by_text("221555232")).not_to_be_visible()
        expect(self.page.get_by_text("brujita75@hotmail.com")).not_to_be_visible()

        expect(self.page.get_by_text("Guido Carrillo")).to_be_visible()
        expect(self.page.get_by_text("1 y 57")).to_be_visible()
        expect(self.page.get_by_text("221232555")).to_be_visible()
        expect(self.page.get_by_text("goleador@gmail.com")).to_be_visible()

        edit_action = self.page.get_by_role("link", name="Editar")
        expect(edit_action).to_have_attribute(
            "href", reverse("clients_edit", kwargs={"id": client.id})
        )

class PetsRepoTestCase(PlaywrightTestCase):
    def test_should_show_message_if_table_is_empty(self):
        self.page.goto(f"{self.live_server_url}{reverse('pets_repo')}")

        expect(self.page.get_by_text("No existen mascotas")).to_be_visible()

    def test_should_show_pets_data(self):
        Pet.objects.create(
            name="gatito",
            breed="orange",
            birthday="2024-05-18",
        )

        Pet.objects.create(
            name="mishu",
            breed="mestizo",
            birthday="2024-04-10",
        )

        self.page.goto(f"{self.live_server_url}{reverse('pets_repo')}")

        expect(self.page.get_by_text("No existen mascotas")).not_to_be_visible()

        expect(self.page.get_by_text("gatito")).to_be_visible()
        expect(self.page.get_by_text("orange")).to_be_visible()
        expect(self.page.get_by_text("May 18, 2024")).to_be_visible()

        expect(self.page.get_by_text("mishu")).to_be_visible()
        expect(self.page.get_by_text("mestizo")).to_be_visible()
        expect(self.page.get_by_text("April 10, 2024")).to_be_visible()

    def test_should_show_add_pet_action(self):
        self.page.goto(f"{self.live_server_url}{reverse('pets_repo')}")

        add_client_action = self.page.get_by_role(
            "link", name="Nueva Mascota", exact=False
        )
        expect(add_client_action).to_have_attribute("href", reverse("pets_form"))

    def test_should_show_pet_edit_action(self):
        pet = Pet.objects.create(
            name="gatito",
            breed="orange",
            birthday="2024-05-18",
        )

        self.page.goto(f"{self.live_server_url}{reverse('pets_repo')}")

        edit_action = self.page.get_by_role("link", name="Editar")
        expect(edit_action).to_have_attribute(
            "href", reverse("pets_edit", kwargs={"id": pet.id})
        )

    def test_should_show_pet_delete_action(self):
        pet = Pet.objects.create(
            name="gatito",
            breed="orange",
            birthday="2024-05-18",
        )

        self.page.goto(f"{self.live_server_url}{reverse('pets_repo')}")

        edit_form = self.page.get_by_role(
            "form", name="Formulario de eliminación de mascotas" 
        )
        pet_id_input = edit_form.locator("input[name=pet_id]")

        expect(edit_form).to_be_visible()
        expect(edit_form).to_have_attribute("action", reverse("pets_delete"))
        expect(pet_id_input).not_to_be_visible()
        expect(pet_id_input).to_have_value(str(pet.id))
        expect(edit_form.get_by_role("button", name="Eliminar")).to_be_visible()

    def test_should_be_able_to_delete_a_pet(self):
        Pet.objects.create(
            name="gatito",
            breed="orange",
            birthday="2024-05-18",
        )

        self.page.goto(f"{self.live_server_url}{reverse('pets_repo')}")

        expect(self.page.get_by_text("gatito")).to_be_visible()

        def is_delete_response(response):
            return response.url.find(reverse("pets_delete"))

        # verificamos que el envio del formulario fue exitoso
        with self.page.expect_response(is_delete_response) as response_info:
            self.page.get_by_role("button", name="Eliminar").click()

        response = response_info.value
        self.assertTrue(response.status < 400) #si es menor es exitoso

        expect(self.page.get_by_text("gatito")).not_to_be_visible()

class PetCreateEditTestCase(PlaywrightTestCase):
    def test_should_be_able_to_create_a_new_pet(self):
        self.page.goto(f"{self.live_server_url}{reverse('pets_form')}")

        expect(self.page.get_by_role("form")).to_be_visible()

        self.page.get_by_label("Nombre").fill("gatito")
        self.page.get_by_label("Raza").fill("orange")
        self.page.get_by_label("Fecha de Nacimiento").fill("2024-05-18")

        self.page.get_by_role("button", name="Guardar").click()

        expect(self.page.get_by_text("gatito")).to_be_visible()
        expect(self.page.get_by_text("orange")).to_be_visible()
        expect(self.page.get_by_text("May 18, 2024")).to_be_visible()

    def test_should_view_errors_if_form_is_invalid(self):
        self.page.goto(f"{self.live_server_url}{reverse('pets_form')}")

        expect(self.page.get_by_role("form")).to_be_visible()

        self.page.get_by_role("button", name="Guardar").click()

        expect(self.page.get_by_text("Por favor ingrese un nombre")).to_be_visible()
        expect(self.page.get_by_text("Por favor ingrese una raza")).to_be_visible()
        expect(self.page.get_by_text("Por favor ingrese una fecha de nacimiento valida y anterior a la de hoy")).to_be_visible()
        
        self.page.get_by_label("Nombre").fill("gatito")
        self.page.get_by_label("Raza").fill("orange")
        self.page.get_by_label("Fecha de Nacimiento").fill("2024-05-18")

        self.page.get_by_role("button", name="Guardar").click()

        expect(self.page.get_by_text("Por favor ingrese un nombre")).not_to_be_visible()
        expect(self.page.get_by_text("Por favor ingrese una raza")).not_to_be_visible()
        expect(self.page.get_by_text("Por favor ingrese una fecha de nacimiento valida y anterior a la de hoy")).not_to_be_visible()

    def test_should_view_error_if_birthday_is_today(self):
        date_now = datetime.date.today().strftime("%Y-%m-%d")

        self.page.goto(f"{self.live_server_url}{reverse('pets_form')}")

        expect(self.page.get_by_role("form")).to_be_visible()

        self.page.get_by_label("Nombre").fill("gatito")
        self.page.get_by_label("Raza").fill("orange")
        self.page.get_by_label("Fecha de Nacimiento").fill(date_now)

        self.page.get_by_role("button", name="Guardar").click()

        expect(self.page.get_by_text("Por favor ingrese una fecha de nacimiento valida y anterior a la de hoy")).to_be_visible()

        self.page.get_by_label("Nombre").fill("gatito")
        self.page.get_by_label("Raza").fill("orange")
        self.page.get_by_label("Fecha de Nacimiento").fill("2024-05-18")

        self.page.get_by_role("button", name="Guardar").click()

        expect(self.page.get_by_text("Por favor ingrese una fecha de nacimiento valida y anterior a la de hoy")).not_to_be_visible()

    def test_should_view_error_if_birthday_is_later_than_today(self): 
        date_now = datetime.date.today()
        date_later = date_now + datetime.timedelta(days=1)
        date = date_later.strftime("%Y-%m-%d")

        self.page.goto(f"{self.live_server_url}{reverse('pets_form')}")

        expect(self.page.get_by_role("form")).to_be_visible()

        self.page.get_by_label("Nombre").fill("gatito")
        self.page.get_by_label("Raza").fill("orange")
        self.page.get_by_label("Fecha de Nacimiento").fill(date)

        self.page.get_by_role("button", name="Guardar").click()

        expect(self.page.get_by_text("Por favor ingrese una fecha de nacimiento valida y anterior a la de hoy")).to_be_visible()

        self.page.get_by_label("Nombre").fill("gatito")
        self.page.get_by_label("Raza").fill("orange")
        self.page.get_by_label("Fecha de Nacimiento").fill("2024-05-18")

        self.page.get_by_role("button", name="Guardar").click()

        expect(self.page.get_by_text("Por favor ingrese una fecha de nacimiento valida y anterior a la de hoy")).not_to_be_visible()

    def test_should_be_able_to_edit_a_pet(self):
        pet = Pet.objects.create(
            name="gatito",
            breed="orange",
            birthday="2024-05-18",
        )

        path = reverse("pets_edit", kwargs={"id": pet.id})
        self.page.goto(f"{self.live_server_url}{path}")

        self.page.get_by_label("Nombre").fill("mishu")
        self.page.get_by_label("Raza").fill("mestizo")
        self.page.get_by_label("Fecha de Nacimiento").fill("2024-04-10")

        self.page.get_by_role("button", name="Guardar").click()

        expect(self.page.get_by_text("gatito")).not_to_be_visible()
        expect(self.page.get_by_text("orange")).not_to_be_visible()
        expect(self.page.get_by_text("May 18, 2024")).not_to_be_visible()

        expect(self.page.get_by_text("mishu")).to_be_visible()
        expect(self.page.get_by_text("mestizo")).to_be_visible()
        expect(self.page.get_by_text("April 10, 2024")).to_be_visible()

        edit_action = self.page.get_by_role("link", name="Editar")
        expect(edit_action).to_have_attribute(
            "href", reverse("pets_edit", kwargs={"id": pet.id})
        )

    def test_should_not_be_able_to_edit_pet_if_form_is_invalid(self):
        pet = Pet.objects.create(
            name="gatito",
            breed="orange",
            birthday="2024-05-18",
        )

        path = reverse("pets_edit", kwargs={"id": pet.id})
        self.page.goto(f"{self.live_server_url}{path}")

        self.page.get_by_label("Nombre").fill("")
        self.page.get_by_label("Raza").fill("")
        self.page.get_by_label("Fecha de Nacimiento").fill("")

        self.page.get_by_role("button", name="Guardar").click()

        expect(self.page.get_by_text("Por favor ingrese un nombre")).to_be_visible()
        expect(self.page.get_by_text("Por favor ingrese una raza")).to_be_visible()
        expect(self.page.get_by_text("Por favor ingrese una fecha de nacimiento valida y anterior a la de hoy")).to_be_visible()

        self.page.get_by_label("Nombre").fill("mishu")
        self.page.get_by_label("Raza").fill("mestizo")
        self.page.get_by_label("Fecha de Nacimiento").fill("2024-04-10")

        self.page.get_by_role("button", name="Guardar").click()

        expect(self.page.get_by_text("Por favor ingrese un nombre")).not_to_be_visible()
        expect(self.page.get_by_text("Por favor ingrese una raza")).not_to_be_visible()
        expect(self.page.get_by_text("Por favor ingrese una fecha de nacimiento valida y anterior a la de hoy")).not_to_be_visible()

        expect(self.page.get_by_text("gatito")).not_to_be_visible()
        expect(self.page.get_by_text("orange")).not_to_be_visible()
        expect(self.page.get_by_text("May 18, 2024")).not_to_be_visible()

        expect(self.page.get_by_text("mishu")).to_be_visible()
        expect(self.page.get_by_text("mestizo")).to_be_visible()
        expect(self.page.get_by_text("April 10, 2024")).to_be_visible()

        edit_action = self.page.get_by_role("link", name="Editar")
        expect(edit_action).to_have_attribute(
            "href", reverse("pets_edit", kwargs={"id": pet.id})
        )

    def test_should_not_be_able_to_edit_pet_if_birthday_is_today(self):
        pet = Pet.objects.create(
            name="gatito",
            breed="orange",
            birthday="2024-05-18",
        )

        path = reverse("pets_edit", kwargs={"id": pet.id})
        self.page.goto(f"{self.live_server_url}{path}")

        date_now = datetime.date.today().strftime("%Y-%m-%d")

        self.page.get_by_label("Nombre").fill("gatito")
        self.page.get_by_label("Raza").fill("orange")
        self.page.get_by_label("Fecha de Nacimiento").fill(date_now)

        self.page.get_by_role("button", name="Guardar").click()

        expect(self.page.get_by_text("Por favor ingrese una fecha de nacimiento valida y anterior a la de hoy")).to_be_visible()

        self.page.get_by_label("Nombre").fill("gatito")
        self.page.get_by_label("Raza").fill("orange")
        self.page.get_by_label("Fecha de Nacimiento").fill("2024-04-10")

        self.page.get_by_role("button", name="Guardar").click()

        expect(self.page.get_by_text("Por favor ingrese una fecha de nacimiento valida y anterior a la de hoy")).not_to_be_visible()

        expect(self.page.get_by_text("gatito")).to_be_visible()
        expect(self.page.get_by_text("orange")).to_be_visible()
        expect(self.page.get_by_text("April 10, 2024")).to_be_visible()

        expect(self.page.get_by_text("May 18, 2024")).not_to_be_visible()

        edit_action = self.page.get_by_role("link", name="Editar")
        expect(edit_action).to_have_attribute(
            "href", reverse("pets_edit", kwargs={"id": pet.id})
        )

    def test_should_not_be_able_to_edit_pet_if_birthday_is_later_than_today(self):
        pet = Pet.objects.create(
            name="gatito",
            breed="orange",
            birthday="2024-05-18",
        )

        path = reverse("pets_edit", kwargs={"id": pet.id})
        self.page.goto(f"{self.live_server_url}{path}")

        date_now = datetime.date.today()
        date_later = date_now + datetime.timedelta(days=1)
        date = date_later.strftime("%Y-%m-%d")

        self.page.get_by_label("Nombre").fill("gatito")
        self.page.get_by_label("Raza").fill("orange")
        self.page.get_by_label("Fecha de Nacimiento").fill(date)

        self.page.get_by_role("button", name="Guardar").click()

        expect(self.page.get_by_text("Por favor ingrese una fecha de nacimiento valida y anterior a la de hoy")).to_be_visible()

        self.page.get_by_label("Nombre").fill("gatito")
        self.page.get_by_label("Raza").fill("orange")
        self.page.get_by_label("Fecha de Nacimiento").fill("2024-04-10")

        self.page.get_by_role("button", name="Guardar").click()

        expect(self.page.get_by_text("Por favor ingrese una fecha de nacimiento valida y anterior a la de hoy")).not_to_be_visible()

        expect(self.page.get_by_text("gatito")).to_be_visible()
        expect(self.page.get_by_text("orange")).to_be_visible()
        expect(self.page.get_by_text("April 10, 2024")).to_be_visible()

        expect(self.page.get_by_text("May 18, 2024")).not_to_be_visible()

        edit_action = self.page.get_by_role("link", name="Editar")
        expect(edit_action).to_have_attribute(
            "href", reverse("pets_edit", kwargs={"id": pet.id})
        )