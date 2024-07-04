import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCreaGrafo(self, e):
        print("controller crea grafo")
        durata = self._view._txtInDurata.value
        self._model.creaGrafo(durata)
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                 f"{self._model.getNumNodes()} nodi."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                 f"{self._model.getNumEdges()} archi."))
        self._view.update_page()
        self.fillDropdown()

    def getSelectedAlbum(self, e):
        pass

    def handleAnalisiComp(self, e):
        idAlbum = self._view._ddAlbum.value

        sizeConnessa = self._model.getConnessa(idAlbum)

        self._view._txt_result.controls.append(
            ft.Text(f"La componente connessa che contiene {idAlbum} ha dimesione {sizeConnessa}.")
        )

    def handleGetSetAlbum(self, e):
        pass

    def fillDropdown(self):
        nodi = self._model._idMap.values()
        for nodo in nodi:
            self._view._ddAlbum.options.append(ft.dropdown.Option(key=nodo.albumId, text=nodo))
        self._view.update_page()

