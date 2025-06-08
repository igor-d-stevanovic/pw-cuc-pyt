from playwright.sync_api import sync_playwright

def before_all(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(
        headless=True,
        args=["--start-maximized"]
    )

def before_scenario(context, scenario):
    print("before_scenario: creating page")
    # Set viewport to None to allow window to be maximized
    context.page = context.browser.new_page(viewport=None)

def after_scenario(context, scenario):
    context.page.close()

def after_all(context):
    context.browser.close()
    context.playwright.stop()