class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_array(self, array):
        return (f"\n - "+f"\n - ".join(array)) if len(array)>0 else f"\nNone"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}\n"
            f"\nAuthors: {self._stringify_array(self.authors)}\n"
            f"\nDependencies: {self._stringify_array(self.dependencies)}\n"
            f"\nDevelopment dependencies: {self._stringify_array(self.dev_dependencies)}"
        )
