# base/dispatcher.py
class Dispatcher:
    def __init__(self, page):
        self.page = page

    def execute(self, steps: list[dict]):
        """
        steps = [
            {"sName": "username", "configs": [{"action": "setValue", "value": "testuser"}]},
            {"sName": "password", "configs": [{"action": "setValue", "value": "pass123"}]},
            {"sName": "loginBtn", "configs": [{"action": "click"}]}
        ]
        """
        for step in steps:
            element = getattr(self.page, step["sName"])
            for config in step["configs"]:
                action = config["action"]
                value = config.get("value")

                if action == "click":
                    element.click()
                elif action == "setValue":
                    element.set_value(value)
                elif action == "validateText":
                    element.validate_text(value)
                else:
                    raise Exception(f"Unknown action: {action}")