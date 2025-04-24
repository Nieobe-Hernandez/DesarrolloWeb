import React, { useState, useEffect } from "react";
import axios from "axios";
import { Form, Button, Container, Row, Col } from "react-bootstrap";
import { useNavigate } from "react-router-dom";
import { motion } from "framer-motion";

const CustomUserForm = () => {
  const [loading, setLoading] = useState(true);
  const [errors, setErrors] = useState({});
  const [formFields, setFormFields] = useState([]);
  const [formData, setFormData] = useState({
    email: "",
    password: "",
    name: "",
    surname: "",
    control_number: "",
    age: "",
    tel: "",
    address:"",
  });
  const nav = useNavigate();

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/users/form/")
      .then((response) => {
        console.log("Datos del formulario", response.data);
        setFormFields(response.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error(
          "Error al obtener los datos, contacte con el administrador",
          error
        );
        setLoading(false);
      });
  }, []);

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    setLoading(true);
    // Enviar la solicitud POST para registrar el usuario
    axios
      .post("http://127.0.0.1:8000/users/form/", formData)
      .then((response) => {
        alert(response.data.message); // Mensaje de éxito
        setErrors({}); // Limpiar errores en caso de éxito
        setLoading(false);
        nav("/login");
      })
      .catch((error) => {
        if (error.response && error.response.data) {
          setErrors(error.response.data); // Guardamos los errores en el estado
        } else {
          alert("Ocurrio un error inesperado, contacta al administrador.");
        }
        console.error("Error al enviar el formulario", error);
        setLoading(false);
        window.scrollTo(0, 0);
      });
  };

  if(loading){
    return (
        <div className="d-flex justify-content-center align-items-center vh-100">
          <div className="spinner-border text-primary" style={{ width: "5rem", height: "5rem" }} role="status">
            <span className="visually-hidden">Cargando...</span>
          </div>
        </div>
      );
  }

  return (
    <Container className="mt-5 vh-100">
      <Row className="justify-content-md-center">
        <Col md={6}>
          <h2 className="text-center mb-4">Nuevo Usuario</h2>

          <Form onSubmit={handleSubmit}>
            {formFields &&
              Object.keys(formFields).map((field) => {
                const { label, input, type } = formFields[field];

                return (
                  <Form.Group key={field} className="mb-3">
                    <Form.Label>{label}</Form.Label>
                    <Form.Control
                      {...input}
                      value={formData[field] || ""}
                      onChange={handleInputChange}
                      name={field}
                      type={type || "text"}
                    />
                    {field === "password" && (
                      <Form.Text className="text-muted">
                        <ul className="small">
                          <li>Al menos un número.</li>
                          <li>Al menos una letra mayúscula.</li>
                          <li>Al menos un carácter especial (!#$%&?).</li>
                          <li>Mínimo de 8 caracteres en total.</li>
                        </ul>
                      </Form.Text>
                    )}
                    {errors[field] && (
                    <span autoFocus className="text-danger">
                        {errors[field].map((errorMsg, index) => (
                            <span>
                            <i className="bi bi-exclamation-circle-fill me-1"></i>
                            {errorMsg}
                            </span>
                        ))}
                    </span>
                    )}
                  </Form.Group>
                );
              })}
            <Button variant="primary" type="submit" className="w-100 mt-3">
              Enviar
            </Button>
          </Form>
        </Col>
      </Row>
    </Container>
  );
};

export default CustomUserForm;