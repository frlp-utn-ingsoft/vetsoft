import os

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from playwright.sync_api import sync_playwright, expect, Browser

from django.urls import reverse

from app.models import Product

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
playwright = sync_playwright().start()
headless = os.environ.get("HEADLESS", 1) == 1
#headless = os.environ.get("HEADLESS", "0") == 1
slow_mo = os.environ.get("SLOW_MO", 0)


class PlaywrightTestCase(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.browser: Browser = playwright.firefox.launch(
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
    
    def test_should_have_home_cards_with_links(self):
        self.page.goto(self.live_server_url)

        home_products_link = self.page.get_by_test_id("home-Productos")

        expect(home_products_link).to_be_visible()
        expect(home_products_link).to_have_text("Productos")
        expect(home_products_link).to_have_attribute("href", reverse("products_repo"))


class ProductsRepoTestCase(PlaywrightTestCase):
    def test_should_show_message_if_table_is_empty(self):
        self.page.goto(f"{self.live_server_url}{reverse('products_repo')}")

        expect(self.page.get_by_text("No existen productos")).to_be_visible()

    def test_should_show_products_data(self):
        Product.objects.create(
            name="Producto A",
            type="Tipo A",
            price=100.0,
        )

        Product.objects.create(
            name="Producto B",
            type="Tipo B",
            price=200.0,
        )

        self.page.goto(f"{self.live_server_url}{reverse('products_repo')}")

        expect(self.page.get_by_text("No existen productos")).not_to_be_visible()

        expect(self.page.get_by_text("Producto A")).to_be_visible()
        expect(self.page.get_by_text("Tipo A")).to_be_visible()
        expect(self.page.get_by_text("100.0")).to_be_visible()

        expect(self.page.get_by_text("Producto B")).to_be_visible()
        expect(self.page.get_by_text("Tipo B")).to_be_visible()
        expect(self.page.get_by_text("200.0")).to_be_visible()

    def test_should_show_add_product_action(self):
        self.page.goto(f"{self.live_server_url}{reverse('products_repo')}")

        add_product_action = self.page.get_by_role(
            "link", name="Nuevo producto", exact=False
        )
        expect(add_product_action).to_have_attribute("href", reverse("products_form"))

    def test_should_show_product_edit_action(self):
        product = Product.objects.create(
            name="Producto A",
            type="Tipo A",
            price=100.0,
        )

        self.page.goto(f"{self.live_server_url}{reverse('products_repo')}")

        edit_action = self.page.get_by_role("link", name="Editar")
        expect(edit_action).to_have_attribute(
            "href", reverse("products_edit", kwargs={"id": product.id})
        )

    def test_should_show_product_delete_action(self):
        product = Product.objects.create(
            name="Producto A",
            type="Tipo A",
            price=100.0,
        )

        self.page.goto(f"{self.live_server_url}{reverse('products_repo')}")

        edit_form = self.page.get_by_role(
            "form", name="Formulario de eliminación de producto"
        )
        product_id_input = edit_form.locator("input[name=product_id]")

        expect(edit_form).to_be_visible()
        expect(edit_form).to_have_attribute("action", reverse("products_delete"))
        expect(product_id_input).not_to_be_visible()
        expect(product_id_input).to_have_value(str(product.id))
        expect(edit_form.get_by_role("button", name="Eliminar")).to_be_visible()

    def test_should_can_be_able_to_delete_a_product(self):
        Product.objects.create(
            name="Producto A",
            type="Tipo A",
            price=100.0,
        )

        self.page.goto(f"{self.live_server_url}{reverse('products_repo')}")

        expect(self.page.get_by_text("Producto A")).to_be_visible()

        def is_delete_response(response):
            return response.url.find(reverse("products_delete"))

        # verificamos que el envio del formulario fue exitoso
        with self.page.expect_response(is_delete_response) as response_info:
            self.page.get_by_role("button", name="Eliminar").click()

        response = response_info.value
        self.assertTrue(response.status < 400)

        expect(self.page.get_by_text("Producto A")).not_to_be_visible()


class ProductCreateEditTestCase(PlaywrightTestCase):
    def test_should_be_able_to_create_a_new_product(self):
        self.page.goto(f"{self.live_server_url}{reverse('products_form')}")

        expect(self.page.get_by_role("form")).to_be_visible()

        self.page.get_by_label("Nombre").fill("Producto A")
        self.page.get_by_label("Tipo").fill("Tipo A")
        self.page.get_by_label("Precio").fill("100.0")

        self.page.get_by_role("button", name="Guardar").click()

        expect(self.page.get_by_text("Producto A")).to_be_visible()
        expect(self.page.get_by_text("Tipo A")).to_be_visible()
        expect(self.page.get_by_text("100.0")).to_be_visible()

    def test_should_view_errors_if_form_is_invalid(self):
        self.page.goto(f"{self.live_server_url}{reverse('products_form')}")

        expect(self.page.get_by_role("form")).to_be_visible()

        self.page.get_by_role("button", name="Guardar").click()

        expect(self.page.get_by_text("Por favor ingrese un nombre")).to_be_visible()
        expect(self.page.get_by_text("Por favor ingrese un tipo")).to_be_visible()
        expect(self.page.get_by_text("Por favor ingrese un precio")).to_be_visible()

        self.page.get_by_label("Nombre").fill("Producto A")
        self.page.get_by_label("Tipo").fill("Tipo A")
        self.page.get_by_label("Precio").fill("-100.0")

        self.page.get_by_role("button", name="Guardar").click()

        expect(self.page.get_by_text("Por favor ingrese un nombre")).not_to_be_visible()
        expect(self.page.get_by_text("Por favor ingrese un tipo")).not_to_be_visible()
        expect(self.page.get_by_text("Por favor ingrese un precio mayor a cero")).to_be_visible()

        self.page.get_by_label("Precio").fill("0.0")

        self.page.get_by_role("button", name="Guardar").click()

        expect(self.page.get_by_text("Por favor ingrese un nombre")).not_to_be_visible()
        expect(self.page.get_by_text("Por favor ingrese un tipo")).not_to_be_visible()
        expect(self.page.get_by_text("Por favor ingrese un precio mayor a cero")).to_be_visible()

    def test_should_be_able_to_edit_a_product(self):
        product = Product.objects.create(
            name="Producto A",
            type="Tipo A",
            price=100.0,
        )

        path = reverse("products_edit", kwargs={"id": product.id})
        self.page.goto(f"{self.live_server_url}{path}")

        self.page.get_by_label("Nombre").fill("Producto B")
        self.page.get_by_label("Tipo").fill("Tipo B")
        self.page.get_by_label("Precio").fill("200.0")

        self.page.get_by_role("button", name="Guardar").click()

        expect(self.page.get_by_text("Producto A")).not_to_be_visible()
        expect(self.page.get_by_text("Tipo A")).not_to_be_visible()
        expect(self.page.get_by_text("100.0")).not_to_be_visible()

        expect(self.page.get_by_text("Producto B")).to_be_visible()
        expect(self.page.get_by_text("Tipo B")).to_be_visible()
        expect(self.page.get_by_text("200.0")).to_be_visible()

        edit_action = self.page.get_by_role("link", name="Editar")
        expect(edit_action).to_have_attribute(
            "href", reverse("products_edit", kwargs={"id": product.id})
        )
