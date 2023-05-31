import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.12
import QtQuick.Controls.Material 2.15
import QtQuick3D 1.15

ApplicationWindow {
    visible: true
    width: 800
    height: 600
    title: "QtQuick 3D Example"

    // Ana Container
    Item {
        anchors.fill: parent

        // Dikey düzen
        ColumnLayout {
            anchors.fill: parent

            // Canvas3D elemanı
            Canvas3D {
                id: canvas3D
                Layout.fillWidth: true
                Layout.fillHeight: true
                objectName: "canvas3D"
                antialiasing: true

                // Verileri almak için 'data' özelliği
                property variant data: []
            }
        }
    }
}
