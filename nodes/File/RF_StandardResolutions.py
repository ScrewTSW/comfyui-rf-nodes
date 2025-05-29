class RF_StandardResolutions:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "value": (["Standard 1:1 (512x512)",
                        "Standard 1:1 (720x720)",
                        "Standard 1:1 (1024x1024)",
                        "Standard 1:1 (1448x1448)",
                        "Widescreen 4:3 (1152x896)",
                        "Widescreen 4:3 (1664x1216)",
                        "Widescreen 3:2 (944x640)",
                        "Widescreen 3:2 (1056x720)",
                        "Widescreen 3:2 (1216x832)",
                        "Widescreen 3:2 (1728x1152)",
                        "Widescreen 4:5 (1280x1024)",
                        "Widescreen 16:9 (424x240)",
                        "Widescreen 16:9 (640x360)",
                        "Widescreen 16:9 (856x480)",
                        "Widescreen 16:9 (1280x720)",
                        "Widescreen 16:9 (1368x768)",
                        "Widescreen 16:9 (1920x1080)",
                        "Widescreen 21:9 (1568x672)",
                        "Widescreen 21:9 (2176x960)",
                        "Widescreen 0.8:1 (640x512)",
                        "Widescreen 0.8:1 (960x768)",
                        "Widescreen 0.8:1 (1120x896)",
                        "Widescreen 0.8:1 (1280x1024)",
                        "Widescreen 0.8:1 (1600x1280)",
                        "Widescreen 0.8:1 (1920x1536)",
                        "Portrait 4:3 (896x1152)",
                        "Portrait 4:3 (1216x1664)",
                        "Portrait 3:2 (640x944)",
                        "Portrait 3:2 (720x1056)",
                        "Portrait 3:2 (832x1216)",
                        "Portrait 3:2 (1152x1728)",
                        "Portrait 4:5 (1024x1280)",
                        "Portrait 16:9 (240x424)",
                        "Portrait 16:9 (360x640)",
                        "Portrait 16:9 (480x856)",
                        "Portrait 16:9 (720x1280)",
                        "Portrait 16:9 (768x1368)",
                        "Portrait 16:9 (1080x1920)",
                        "Portrait 21:9 (1568x672)",
                        "Portrait 21:9 (960x2176)",
                        "Portrait 0.8:1 (512x640)",
                        "Portrait 0.8:1 (768x960)",
                        "Portrait 0.8:1 (896x1120)",
                        "Portrait 0.8:1 (1024x1280)",
                        "Portrait 0.8:1 (1280x1600)",
                        "Portrait 0.8:1 (1536x1920)"], {
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
        match value:
            case "Standard 1:1 (512x512)":
                return (512, 512)
            case "Standard 1:1 (720x720)":
                return (720, 720)
            case "Standard 1:1 (1024x1024)":
                return (1024, 1024)
            case "Standard 1:1 (1448x1448)":
                return (1448, 1448)
            case "Widescreen 4:3 (1152x896)":
                return (1152, 896)
            case "Widescreen 4:3 (1664x1216)":
                return (1664, 1216)
            case "Widescreen 3:2 (944x640)":
                return (944, 640)
            case "Widescreen 3:2 (1056x720)":
                return (1056, 720)
            case "Widescreen 3:2 (1216x832)":
                return (1216, 832)
            case "Widescreen 3:2 (1728x1152)":
                return (1728, 1152)
            case "Widescreen 4:5 (1280x1024)":
                return (1280, 1024)
            case "Widescreen 16:9 (424x240)":
                return (424, 240)
            case "Widescreen 16:9 (640x360)":
                return (640, 360)
            case "Widescreen 16:9 (856x480)":
                return (856, 480)
            case "Widescreen 16:9 (1280x720)":
                return (1280, 720)
            case "Widescreen 16:9 (1368x768)":
                return (1368, 768)
            case "Widescreen 16:9 (1920x1080)":
                return (1920, 1080)
            case "Widescreen 21:9 (1568x672)":
                return (1568, 672)
            case "Widescreen 21:9 (2176x960)":
                return (2176, 960)
            case "Widescreen 0.8:1 (640x512)":
                return (640, 512)
            case "Widescreen 0.8:1 (960x768)":
                return (960, 768)
            case "Widescreen 0.8:1 (1120x896)":
                return (1120, 896)
            case "Widescreen 0.8:1 (1280x1024)":
                return (1280, 1024)
            case "Widescreen 0.8:1 (1600x1280)":
                return (1600, 1280)
            case "Widescreen 0.8:1 (1920x1536)":
                return (1920, 1536)
            case "Portrait 4:3 (896x1152)":
                return (896, 1152)
            case "Portrait 4:3 (1216x1664)":
                return (1216, 1664)
            case "Portrait 3:2 (640x944)":
                return (640, 944)
            case "Portrait 3:2 (720x1056)":
                return (720, 1056)
            case "Portrait 3:2 (832x1216)":
                return (832, 1216)
            case "Portrait 3:2 (1152x1728)":
                return (1152, 1728)
            case "Portrait 4:5 (1024x1280)":
                return (1024, 1280)
            case "Portrait 16:9 (240x424)":
                return (240, 424)
            case "Portrait 16:9 (360x640)":
                return (360, 640)
            case "Portrait 16:9 (480x856)":
                return (480, 856)
            case "Portrait 16:9 (720x1280)":
                return (720, 1280)
            case "Portrait 16:9 (768x1368)":
                return (768, 1368)
            case "Portrait 16:9 (1080x1920)":
                return (1080, 1920)
            case "Portrait 21:9 (1568x672)":
                return (1568, 672)
            case "Portrait 21:9 (960x2176)":
                return (960, 2176)
            case "Portrait 0.8:1 (512x640)":
                return (512, 640)
            case "Portrait 0.8:1 (768x960)":
                return (768, 960)
            case "Portrait 0.8:1 (896x1120)":
                return (896, 1120)
            case "Portrait 0.8:1 (1024x1280)":
                return (1024, 1280)
            case "Portrait 0.8:1 (1280x1600)":
                return (1280, 1600)
            case "Portrait 0.8:1 (1536x1920)":
                return (1536, 1920)
            case _:
                return (1024, 1024)
