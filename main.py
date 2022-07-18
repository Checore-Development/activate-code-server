import activate_code_server

server = activate_code_server.app_server(
    host='localhost',
    port=7000,
    database_engine='sqlite3',
    database_filename='database',
    database_name='activate_code_server'
)

if __name__ == "__main__":
    server.setup_blueprint(activate_code_server.app)
    server.run()