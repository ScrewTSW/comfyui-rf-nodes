import random


class RF_FloatRangePrimitive:

    rangeMin = 0.0
    rangeMax = 1.0
    step = 0.00001
    value = 1.0
    actionAfterRender = "DO_NOTHING"

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "rangeMin": ("FLOAT", {
                    "forceInput": False,
                    "default": 0.0,
                    "step": 0.00001,
                    "round": False,
                    "display": "number",
                }),
                "rangeMax": ("FLOAT", {
                    "forceInput": False,
                    "default": 1.0,
                    "step": 0.00001,
                    "round": False,
                    "display": "number",
                }),
                "step": ("FLOAT", {
                    "forceInput": False,
                    "default": 0.00001,
                    "step": 0.00001,
                    "round": False,
                    "display": "number",
                }),
                "value": ("FLOAT", {
                    "forceInput": False,
                    "rangeMin": s.rangeMin,
                    "rangeMax": s.rangeMax,
                    "default": s.value,
                    "step": s.step,
                    "round": False,
                    "display": "slider",
                }),
                "actionAfterRender": ( ["DO_NOTHING", "INCREMENT", "DECREMENT", "RANDOMIZE"], {
                    "forceInput": False,
                    "default": "DO_NOTHING",
                })
            },
        }

    DISPLAY_NAME = "Float Range Primitive"
    CATEGORY = "RF/primitives"

    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("FLOAT",)

    FUNCTION = "NodeProcess"
    def NodeProcess(self, rangeMin, rangeMax, step, value, actionAfterRender):
        if rangeMin is not None:
            if rangeMin != self.rangeMin:
                self.rangeMin = rangeMin
        if rangeMax is not None:
            if rangeMax != self.rangeMax:
                self.rangeMax = rangeMax
        if step is not None:
            if step != self.step:
                self.step = step
        if value is not None:
            if value != self.value:
                self.value = value
        if actionAfterRender is not None:
            if actionAfterRender != self.actionAfterRender:
                self.actionAfterRender = actionAfterRender

        if self.actionAfterRender == "INCREMENT":
            if self.value + self.step <= self.rangeMax:
                self.value += self.step
        elif self.actionAfterRender == "DECREMENT":
            if self.value - self.step >= self.rangeMin:
                self.value -= self.step
        elif self.actionAfterRender == "RANDOMIZE":
            self.value = random.uniform(self.rangeMin, self.rangeMax)
        return (self.value,)
