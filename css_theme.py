# coding=utf-8

# Dark Theme
cssStyle = """

        QWidget {
            font-size:16px;
            color: #aaa;
            border: 2px solid; 
            border-width:1px; 
            border-style: solid;
            background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #444, stop: 1 #666);
            min-height:24px; 
        }

        QHeaderView::section {
            background-color: #000000;
        }
        QTableView {
            border-radius:8px;
            background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #444, stop: 1 #666);
        }
        QTableView::item:selected {
            background-color: #555555;
        }
        QPushButton:pressed {
            background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(190, 211, 211, 211), stop:1 rgba(176, 176, 176, 255))
        }
        QPushButton {
             background-color: #D3D3D3; border: 1px solid black;
             border-radius: 5px;
        }

        QPushButton:disabled {
            background-color: rgb(170, 170, 127)
        }
        """
