from diagrams import Diagram, Cluster
from diagrams.aws.iot import IotCamera
from diagrams.onprem.compute import Server
from diagrams.programming.language import Python
from diagrams.onprem.database import Postgresql
from diagrams.generic.storage import Storage
from diagrams.programming.framework import Flask, Flutter

with Diagram("Intelligent Parking Management", show=False):
    with Cluster("Edge AI and Detection"):
        camera = IotCamera("Camera")
        raspberry_pi = Server("Raspberry Pi")
        main = Python("Main")
        bg_detection = Python("BG-Based Detection")
        ssd_efficientdet = Python("SSD EfficientDet")
        
        # Connections for detection setup
        camera >> raspberry_pi >> main
        main >> bg_detection
        main >> ssd_efficientdet

    with Cluster("Hosting Lotus VPS Linux"):
        fileServer = Storage("File Storage")

        with Cluster("Docker"):
            finalAi = Python("Final AI")
            database = Postgresql("Database")
            webSocket = Flask("WebSocket")
            api = Server("RESTful API")

            finalAi >> database
            database >> webSocket
            webSocket >> database
            database >> api
            api >> database
        
        fileServer >> webSocket
        webSocket >> fileServer
    
    with Cluster("Client"):
        spot = Flutter("View spots")
        mobile = Flutter("Stream")
        login = Flutter("Login")
        register = Flutter("Register")
    
    raspberry_pi >> fileServer
    bg_detection >> finalAi
    ssd_efficientdet >> finalAi

    webSocket >> mobile
    mobile >> webSocket

    spot >> webSocket
    webSocket >> spot

    login >> api
    register >> api