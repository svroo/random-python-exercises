# IMPORTAMOS LIBRERIAS NECESARIAS
import os
import shutil

# import time
# import schedule

# Definimos la ruta a trabajar
path_origin = "C:/Users/rod_e/Downloads/"

# Definimos las categorias de los archivos donde las llaves son las carpetas que se van a crear
file_extensions = {
    "Multimedia": [
        "mp3",
        "mp4",
        "wav",
        "avi",
        "mkv",
        "mov",
        "flac",
        "aac",
        "wma",
        "wmv",
    ],
    "Imagenes": ["jpg", "jpeg", "png", "gif", "bmp", "tiff", "svg", "ico", "webp"],
    "Documentos": [
        "pdf",
        "doc",
        "docx",
        # "xls",
        # "xlsx",
        # "ppt",
        # "pptx",
        "txt",
        "rtf",
        "odt",
        "ods",
        "odp",
    ],
    "Compresion": ["zip", "rar", "7z", "tar", "gz", "iso", "bz2"],
    "Codigo_fuente": [
        "py",
        "js",
        "html",
        "css",
        "java",
        "cpp",
        "c",
        "cs",
        "php",
        "rb",
        "go",
        "rs",
        "kt",
        "ts",
        "sh",
        "pl",
    ],
    "Sistema": ["exe", "dll", "sys", "ini", "bat", "msi", "cfg", "reg", "drv"],
    "Bases_de_datos": ["sql", "db", "mdb", "accdb", "sqlite", "dbf", "json", "xml"],
    "Fuentes": ["ttf", "otf", "woff", "woff2", "eot"],
    "Modelos_3d": ["obj", "fbx", "stl", "3ds", "dae", "blend"],
    "Hojas_de_estilo": ["css", "scss", "sass", "less"],
    "Libros_electronicos": ["epub", "mobi", "azw3", "fb2", "lit"],
    "Scripts": ["sh", "bat", "ps1", "vbs", "cmd"],
    "Hojas_de_calculo": ["xls", "xlsx", "csv", "ods", "xlsm"],
    "Presentaciones": ["ppt", "pptx", "odp", "key"],
    "Proyectos_multimedia": ["psd", "ai", "fla", "swf", "prproj", "aep"],
    "Otros": ["log", "bak", "tmp", "md", "torrent"],
}


def ordenar_carpeta(path_o: str, files_and_format: dict):
    """Esta función solo existe para ordenar los archivos usando schedule

    Args:
        path_o (str): Carpeta que queremos ordenar
        files_and_format (dict): Carpetas a crear y archivos que van a contener dichas carpetas (por archivos me refiero a extensiones)
    """
    files = os.listdir(path_o)

    # Empezamos a recorrer los archivos
    for item in files:

        # Comprobamos que es un archivo y no una carpeta
        if "." in item:
            extension = item.split(".")[-1].lower()

            # Empezamos a iterar sobre las llaves del diccionario para ver el contenido de estos
            for key in files_and_format.keys():

                # Checamos si la extensión esta en algún elemento en la parte de valor del diccionario
                if extension in files_and_format[key]:

                    # Creamos la ruta final correspondiente al archivo que vamos a mover y creamos la carpeta
                    path_final = path_o + key + "/"
                    os.makedirs(path_final, exist_ok=True)

                    # Movemos el archivo a la ruta final
                    try:
                        shutil.move(src=path_o + item, dst=path_final)
                    except:
                        pass
                    break
            continue
        else:
            # print("Es una carpeta")
            continue

    # return print("Se terminaron de ordenar los archivos")


if __name__ == "__main__":

    # # Ponemos la hora en la que queremos que se ejecute el archivo
    # schedule.every().monday.at("12:30").do(ordenar_carpeta)

    # # Creamos un ciclo para que se ejecute en segundo plano
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
    ordenar_carpeta(path_o=path_origin, files_and_format=file_extensions)
