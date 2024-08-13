class RF_StandardResolutions:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "value": (["Standard 1:1 (1024x1024)", "Portrait 4:5 (1024x1280)"], {
                    "forceInput": False,
                    "default": "Standard 1:1 (1024x1024)",
                })
            },
        }

    DISPLAY_NAME = "Standard Resolutions"
    CATEGORY = "RF/file"

    RETURN_TYPES = ("INT","INT",)
    RETURN_NAMES = ("WIDTH","HEIGHT",)

    FUNCTION = "NodeProcess"
    def NodeProcess(self, value):
        if value == "Standard 1:1 (1024x1024)":
            return (1024, 1024)
        elif value == "Portrait 4:5 (1024x1280)":
            return (1024, 1280)
        return (1024, 1024)
