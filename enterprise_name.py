import pyfiglet

class EnterpriseName:
    """
    Class responsible for returning the company name in a stylized way.
    """

    @staticmethod
    def display_company_name():
        """
        Returns the company name in a stylized format using pyfiglet.
        """
        ascii_art = pyfiglet.figlet_format("FARM TECH SOLUTION")
        return "\n🌿 🌱\n" + ascii_art + "🌱 🌿\n"