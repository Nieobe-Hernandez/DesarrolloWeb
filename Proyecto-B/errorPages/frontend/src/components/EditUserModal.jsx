import React, { useState, useEffect } from "react";
import { Modal, Button, Form, Alert } from "react-bootstrap";
import userService from "../services/userService";

const EditUserModal = ({ show, onHide, user, onSuccess }) => {
  const [formData, setFormData] = useState({
    email: "",
    name: "",
    surname: "",
    control_number: "",
    age: "",
    tel: "",
    address: ""
  });
  
  const [error, setError] = useState("");
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [showConfirm, setShowConfirm] = useState(false);

  useEffect(() => {
    if (user) {
      setFormData({
        email: user.email || "",
        name: user.name || "",
        surname: user.surname || "",
        control_number: user.control_number || "",
        age: user.age || "",
        tel: user.tel || "",
        address: user.address || ""
      });
    }
  }, [user]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };

  const handleSubmit = async () => {
    setShowConfirm(true);
  };

  const confirmUpdate = async () => {
    setIsSubmitting(true);
    setError("");
    try {
      await userService.updateUser(user.id, formData);
      setIsSubmitting(false);
      setShowConfirm(false);
      onSuccess("Usuario actualizado exitosamente");
      onHide();
    } catch (error) {
      setIsSubmitting(false);
      setShowConfirm(false);
      setError(
        error.response?.data?.message ||
        "Error al actualizar el usuario. Inténtalo de nuevo."
      );
    }
  };

  const cancelUpdate = () => {
    setShowConfirm(false);
  };

  return (
    <>
      <Modal show={show} onHide={onHide} centered backdrop="static">
        <Modal.Header closeButton>
          <Modal.Title>Editar Usuario</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          {error && <Alert variant="danger">{error}</Alert>}
          
          <Form>
            <Form.Group className="mb-3">
              <Form.Label>Correo Electrónico</Form.Label>
              <Form.Control
                type="email"
                name="email"
                value={formData.email}
                onChange={handleChange}
                required
                pattern="^[a-zA-Z0-9]+@utez\.edu\.mx$"
                placeholder="Ingrese correo electrónico"
              />
            </Form.Group>

            <Form.Group className="mb-3">
              <Form.Label>Nombre</Form.Label>
              <Form.Control
                type="text"
                name="name"
                value={formData.name}
                onChange={handleChange}
                required
                minLength={3}
                maxLength={100}
                placeholder="Ingrese nombre"
              />
            </Form.Group>

            <Form.Group className="mb-3">
              <Form.Label>Apellido</Form.Label>
              <Form.Control
                type="text"
                name="surname"
                value={formData.surname}
                onChange={handleChange}
                required
                minLength={3}
                maxLength={100}
                placeholder="Ingrese apellido"
              />
            </Form.Group>

            <Form.Group className="mb-3">
              <Form.Label>Matrícula</Form.Label>
              <Form.Control
                type="text"
                name="control_number"
                value={formData.control_number}
                onChange={handleChange}
                required
                pattern="^I?[0-9]{5}[A-Za-z]{2}[0-9]{3}$"
                placeholder="Ingrese matrícula"
              />
            </Form.Group>

            <Form.Group className="mb-3">
              <Form.Label>Edad</Form.Label>
              <Form.Control
                type="number"
                name="age"
                value={formData.age}
                onChange={handleChange}
                required
                min={1}
                max={150}
                placeholder="Ingrese edad"
              />
            </Form.Group>

            <Form.Group className="mb-3">
              <Form.Label>Teléfono</Form.Label>
              <Form.Control
                type="text"
                name="tel"
                value={formData.tel}
                onChange={handleChange}
                required
                pattern="^[0-9]{10}$"
                placeholder="Ingrese teléfono"
              />
            </Form.Group>

            <Form.Group className="mb-3">
              <Form.Label>Dirección</Form.Label>
              <Form.Control
                type="text"
                name="address"
                value={formData.address}
                onChange={handleChange}
                required
                minLength={5}
                maxLength={200}
                placeholder="Ingrese dirección"
              />
            </Form.Group>
          </Form>
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={onHide}>
            Cancelar
          </Button>
          <Button 
            variant="primary" 
            onClick={handleSubmit} 
            disabled={isSubmitting}
          >
            {isSubmitting ? "Actualizando..." : "Actualizar Usuario"}
          </Button>
        </Modal.Footer>
      </Modal>

      {/* Modal de confirmación */}
      <Modal show={showConfirm} onHide={cancelUpdate} centered>
        <Modal.Header closeButton>
          <Modal.Title>Confirmar Actualización</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          ¿Estás seguro que deseas actualizar a este usuario?
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={cancelUpdate}>
            Cancelar
          </Button>
          <Button variant="primary" onClick={confirmUpdate}>
            Confirmar
          </Button>
        </Modal.Footer>
      </Modal>
    </>
  );
};

export default EditUserModal;