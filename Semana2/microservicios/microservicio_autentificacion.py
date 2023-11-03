from fastapi import FastAPI

app = FastAPI()

# Definir un usuario y contraseña de administrador (esto podría manejarse de manera más segura en la práctica)
admin_username = "admin"
admin_password = "admin"

@app.post("/login")
def login(username: str, password: str):
    #Verificar si las credenciales son válidas
    if username == admin_username and password == admin_password:
        return {"status": "autorizado"}
    else:
        raise HTTPException(status_code=401, detail="No autorizado")
