import time
import re
from playwright.sync_api import Playwright, sync_playwright


def verifica_placa():
    t0 = time.time()
    while True:
        placa = input('Informe a placa(sem hífen) ou 0 para finalizar:')
        if re.match(r"^[A-Za-z]{3}[0-9]{4}$", placa):
            def run(playwright: Playwright) -> None:
                browser = playwright.chromium.launch(headless=False)
                context = browser.new_context()
                page = context.new_page()
                page.goto("https://intranet.pm.se.gov.br/portal/")
                page.get_by_placeholder("Usuário").fill("01467475505")
                page.get_by_placeholder("Senha").click()
                page.get_by_placeholder("Senha").fill("MGD878")
                page.get_by_role("button", name="Entrar").click()
                page.goto("https://intranet.pm.se.gov.br/portal/consultaVeiculo")
                time.sleep(2)
                page.locator("a").filter(has_text=re.compile(r"^Consulta Veicular$")).click()
                page.get_by_placeholder("Placa").click()
                page.get_by_placeholder("Placa").fill(placa)
                page.get_by_placeholder("Placa").press("Enter")

                time.sleep(5)

                # ---------------------
                context.close()
                browser.close()

            with sync_playwright() as playwright:
                run(playwright)
            print(f'A placa {placa} segue o padrão de placa antiga. AQUI VOU INSERIR OS DADOS DO PORTAL')

        elif re.match(r"^[A-Za-z]{3}[0-9][A-Za-z][0-9]{2}$", placa):
            def run(playwright: Playwright) -> None:
                browser = playwright.chromium.launch(headless=False)
                context = browser.new_context()
                page = context.new_page()
                page.goto("https://intranet.pm.se.gov.br/portal/")
                page.get_by_placeholder("Usuário").fill("01467475505")
                page.get_by_placeholder("Senha").click()
                page.get_by_placeholder("Senha").fill("MGD878")
                page.get_by_role("button", name="Entrar").click()
                page.goto("https://intranet.pm.se.gov.br/portal/consultaVeiculo")
                time.sleep(2)
                page.locator("a").filter(has_text=re.compile(r"^Consulta Veicular$")).click()
                page.get_by_placeholder("Placa").click()
                page.get_by_placeholder("Placa").fill(placa)
                page.get_by_placeholder("Placa").press("Enter")

                time.sleep(5)

                # ---------------------
                context.close()
                browser.close()

            with sync_playwright() as playwright:
                run(playwright)
            print(f'A placa {placa} segue o padrão de placa MERCOSUL. AQUI VOU INSERIR OS DADOS DO PORTAL')
        elif placa == '0':
            print('Consulta Finalizada')
            break
        else:
            print("A entrada não é válida!")

    t1 = time.time()
    print(f'Uso finalizado em {t1 - t0:.2f} segundos')


verifica_placa()
