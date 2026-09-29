from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen


class LoginScreen(Screen):

    def ingresar(self):
        nombre = self.ids.nombre.text

        principal = self.manager.get_screen("principal")
        principal.ids.bienvenida.text = f"Bienvenido, {nombre}"

        perfil = self.manager.get_screen("perfil")
        perfil.ids.nombre_perfil.text = nombre

        self.manager.current = "principal"


class PrincipalScreen(Screen):
    pass


class PerfilScreen(Screen):
    pass


class MarketplaceApp(MDApp):
    pass


MarketplaceApp().run()