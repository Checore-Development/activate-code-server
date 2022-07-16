import activate_code_server

server = activate_code_server.app_server(
    host='localhost',
    port=7000,
    database_engine='sqlite',
    database_filename='database'
)

if __name__ == "__main__":
    server.setup_blueprint(activate_code_server.app)
    server.run()