"""
Un module utilisant Qt pour effectuer des actions et afficher des données.

Ici, la fenetre sert à configurer la génération de templates de fichiers.
"""

from PyQt5 import QtWidgets, uic
import sys
from project_cli import run
import os

# Define function to import external files when using PyInstaller.
def resource_path(relative_path):
    """ 
    Get absolute path to resource, works for dev and for PyInstaller 
    Source: https://stackoverflow.com/questions/37888581/pyinstaller-ui-files-filenotfounderror-errno-2-no-such-file-or-directory
    """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
        print(base_path)
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        # on défini une classe UI qui hérite de QMainWindow de Qt.
        # on doit appeler le constructeur de la classe parente.

        super().__init__()  # Call the inherited classes __init__ method
        print(os.listdir())

        # la description de l'interface graphique est faite dans un fichier UI
        # que l'on modifie et génère avec QtDesigner
        uic.loadUi(
            resource_path("window_handle_templating.ui"), self
        )  # Load the .ui file
        self.show()  # Show the GUI

        # on effectue le lien entre des actions et des réactions.
        # Quand le bouton est cliqué, on appele la fonction connectée.
        self.pushButton.clicked.connect(self.get_file)
        self.pushButton_2.clicked.connect(self.run)
        self.pushButton_3.clicked.connect(bouton_ne_pas_toucher_appuye)

        # on connecte les deux boutons + et - à la création et suppression de lignes
        # du tableau de conditions
        self.pushButton_remove_condition.clicked.connect(self.delete_row_if_needed)
        self.pushButton_add_condition.clicked.connect(
            lambda: self.conditionTable.insertRow(self.conditionTable.rowCount())
        )

        # on définie un attribut permettant de stocker le nom du fichier de template
        self.fname = ""

    def delete_row_if_needed(self):
        if self.conditionTable.rowCount() > 1:
            self.conditionTable.removeRow(self.conditionTable.rowCount() - 1)

    def run(self):
        try:
            self._run()
        except Exception as e:
            print(e)
            self.statusbar.showMessage(f"L'erreur {e} a eu lieu")

    def _run(self):
        """Fonction permettant de réaliser concretement la
        génération des fichiers à partir du template.

        Elle apelle en effet le run du fichier j2.py qui contient le
        code de génération.

        C'est dans cette fonction que l'on lit ce qui est stocké dans les line edit
        et que l'on utilise le fname qui contient le nom du fichier de template.
        """
        self.statusbar.showMessage(f"Running")
        print("1")

        k1_string = self.lineEdit_k1.text()
        k2_string = self.lineEdit_k2.text()
        print("2")
        k1s, k2s = self.get_conditions()
        print("3")
        # appel de la fonction de génération avec les
        # paramètres récupérés dans l'interface graphique
        run(self.fname, k1_string, k2_string, k1s, k2s)
        print("4")
        self.statusbar.showMessage(f"OK, génération effectuée.")

    def get_conditions(self):
        """Pour récupérer les valeurs dans le mini tableur
        on doit les parcourir toutes les cellules et récupérer leur texte.

        Comme on a lu le tableau ligne par lignes et non pas colonnes par colonnes,
        on transpose la liste de listes en utilisant zip(*items).

        On pourrait simplifier cette partie en lisant directement par colonnes...
        """
        items = []
        for row_index in range(self.conditionTable.rowCount()):
            row = []
            for col_index in range(self.conditionTable.columnCount()):
                item = self.conditionTable.item(row_index, col_index)
                row.append(item.text())
            items.append(row)

        # on retourne la transposée pour avoir les conditions (k1s, k2s)
        return zip(*items)

    def get_file(self):
        """Méthode permettant d'ouvrir une fenetre (un QFileDialog) afin de choisir
        un fichier et récupérer son chemin.

        Une fois sélectionné :
            * on affiche son nom en le tronquant s'il est trop long
                et en rajoutant un tooltip sur le nom
                pour conserver la possibilité de le voir
            * on affiche son contenu (s'il est trop long, un ascenseur est ajouté)
            * on enregistre le nom dans un attribut appelé `fname`
        """
        options = QtWidgets.QFileDialog.Options()
        # options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Choisir un fichier",
            "",
            "All Files (*);;Python Files (*.py)",
            options=options,
        )
        if fileName:
            self.fname = fileName
            to_display = fileName
            if len(fileName) > 90:
                # si c'est trop long, on coupe
                to_display = "..." + to_display[-90:]
            self.fname_label.setText(to_display)
            self.fname_label.setToolTip(fileName)
            self.textEdit.setText(open(fileName, encoding="utf8").read())


def bouton_ne_pas_toucher_appuye():
    print("noooooooooonnnn")


# code permettant de lancer une application Qt
# # il suffit de le récuperéer d'internet
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
