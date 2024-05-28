

class Transformer:
    def __init__(self, data, transformation):
        self.data = data
        self.transformation_type = transformation.get("type")
        self.transformation_value = transformation.get("value")

    def process(self):
        if self.transformation_type == "REGEX":
            return self.process_regex()
        return ""

    def process_regex(self):
        return self.data
