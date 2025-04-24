import React, { useState, useEffect } from "react";
import DataTable from "react-data-table-component";
import userService from "../services/userService";
import EditUserModal from "./EditUserModal";
import { Modal, Button, Alert } from "react-bootstrap";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

const UserDataTable = () => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selectedUser, setSelectedUser] = useState(null);
  const [showEditModal, setShowEditModal] = useState(false);
  const [showDeleteConfirm, setShowDeleteConfirm] = useState(false);
  const [userToDelete, setUserToDelete] = useState(null);
  const [currentUserId, setCurrentUserId] = useState(null);

  // Cargar usuarios y obtener el ID del usuario actual
  const loadUsers = async () => {
    try {
      setLoading(true);
      const users = await userService.getAllUsers();
      setData(users);
      setLoading(false);
      
      const userId = userService.getCurrentUserId();
      setCurrentUserId(userId);
    } catch (error) {
      console.error("Error al cargar los datos:", error);
      toast.error("Error al cargar los usuarios");
      setLoading(false);
    }
  };

  useEffect(() => {
    loadUsers();
  }, []);

  const columns = [
    {
      name: "Nombre",
      selector: (row) => (row.name + " " + row.surname),
      sortable: true,
    },
    {
      name: "Email",
      selector: (row) => row.email,
      sortable: true,
    },
    {
      name: "Matrícula",
      selector: (row) => row.control_number,
    },
    {
      name: "Teléfono",
      selector: (row) => row.tel,
    },{
      name:"Dirección",
      selector: (row) => row.address,
    },
    {
      name: "Acciones",
      cell: (row) => (
        <span>
          <button
            className="btn btn-warning me-2"
            onClick={() => handleEditClick(row)}
          >
            <i className="bi bi-pencil"></i>
          </button>
          <button
            className="btn btn-danger me-2 color-danger"
            onClick={() => handleDeleteClick(row)}
            disabled={row.id === currentUserId} 
            title={row.id === currentUserId ? "No puedes eliminar tu propio usuario" : "Eliminar usuario"}
          >
            <i className="bi bi-trash"></i>
          </button>
        </span>
      ),
    },
  ];

  const handleEditClick = (user) => {
    setSelectedUser(user);
    setShowEditModal(true);
  };


  const handleDeleteClick = (user) => {
    if (user.id === currentUserId) {
      toast.warning("No puedes eliminar tu propio usuario");
      return;
    }
    
    setUserToDelete(user);
    setShowDeleteConfirm(true);
  };

  const confirmDelete = async () => {
    try {
      await userService.deleteUser(userToDelete.id);
      setShowDeleteConfirm(false);
      toast.success("Usuario eliminado exitosamente");
      loadUsers(); 
    } catch (error) {
      console.error("Error al eliminar usuario:", error);
      toast.error(
        error.response?.data?.message || 
        "Error al eliminar el usuario"
      );
    }
  };

  const handleUpdateSuccess = (message) => {
    toast.success(message);
    loadUsers(); 
  };

  return (
    <div>
      <ToastContainer position="top-right" autoClose={3000} />
      <h3>Tabla de usuarios</h3>
      <DataTable
        columns={columns}
        data={data}
        progressPending={loading}
        pagination
        highlightOnHover
        pointerOnHover
        responsive
      />

      {/* Modal de edición */}
      <EditUserModal
        show={showEditModal}
        onHide={() => setShowEditModal(false)}
        user={selectedUser}
        onSuccess={handleUpdateSuccess}
      />

      {/* Modal de confirmación para eliminar */}
      <Modal show={showDeleteConfirm} onHide={() => setShowDeleteConfirm(false)} centered>
        <Modal.Header closeButton>
          <Modal.Title>Confirmar Eliminación</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          {userToDelete && (
            <div>
              ¿Estás seguro que deseas eliminar al usuario <strong>{userToDelete.name} {userToDelete.surname}</strong>?
              <br />
              <Alert variant="warning" className="mt-3">
                Esta acción no se puede deshacer.
              </Alert>
            </div>
          )}
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={() => setShowDeleteConfirm(false)}>
            Cancelar
          </Button>
          <Button variant="danger" onClick={confirmDelete}>
            Eliminar
          </Button>
        </Modal.Footer>
      </Modal>
    </div>
  );
};

export default UserDataTable;