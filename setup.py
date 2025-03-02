import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bellman_ford",
    version="0.0.1",
    author="Equipo",
    description="Método numérico que resuelva problemas de optimización convexa de pequeña escala.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joelitam2021/practica-2-primera-parte-joelitam2021-fork",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[
        'numpy>=1.19.2'
        ],
    python_requires=">=3.7.12",
)
