admin_permissions = {
    "read",
    "write",
    "delete",
    "manage_users"
}

editor_permissions = {
    "read",
    "write"
}

required_permission = "delete"

if required_permission in editor_permissions:
    print("Access Granted")

else:
    print("Access Denied")