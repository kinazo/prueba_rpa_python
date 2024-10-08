from scripts import api_handling, webscraping, desktop_automation
import subprocess

def run_powershell_script():
    """Ejecuta un script de PowerShell desde Python."""
    subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", "scripts/powershell_script.ps1"])

def main():
    # Ejecutar script de PowerShell
    run_powershell_script()

    # Crear y consumir APIs
    api_handling.create_api()
    api_handling.consume_api()

    # Webscraping con Selenium
    webscraping.scrape_website()

    # Automatización de escritorio con Pywinauto
    desktop_automation.run_desktop_task()

if __name__ == "__main__":
    main()
