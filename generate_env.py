import secrets

with open('.env', 'w') as f:
    f.write(f"SECRET={secrets.token_hex(32)}\n")
    f.write(f"DB_URI=sqlite:///database.db\n")
    
    