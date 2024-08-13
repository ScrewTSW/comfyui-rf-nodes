class TextLine:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "index": ("INT", { }),
                "value": ("STRING", {
                    "multiline": True,
                }),
            },
        }

    CATEGORY = "RF/text"

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("line",)

    FUNCTION = "NodeProcess"
    def NodeProcess(self, index, value):
        lines = value.split("\n")
        return lines[index % len(lines)]
