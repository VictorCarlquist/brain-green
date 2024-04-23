import { useState } from 'react';
import { Form, Button, Card } from 'react-bootstrap';
import { useAddProducerMutation } from '../../redux/reducers/api';

function ProducerFormNew() {
    const [name, setName] = useState("");
    const [cpfCnpj, setCpfCnpj] = useState("");
    const [producerAdd] = useAddProducerMutation();

    return (
        <Card body>
            <Form>
                <Form.Group controlId="name">
                    <Form.Label>Nome do Produtor</Form.Label>
                    <Form.Control type="text" placeholder="Nome do Produtor" value={name} onChange={(e) => setName(e.target.value)} />
                </Form.Group>

                <Form.Group controlId="cpfCnpj">
                    <Form.Label>CPF/CNPJ</Form.Label>
                    <Form.Control type="text" placeholder="CPF/CNPJ" value={cpfCnpj} onChange={(e) => setCpfCnpj(e.target.value)} />
                </Form.Group>

                <Button variant="primary" onClick={() => {
                    const producer_data = {
                        name: name,
                        cpf_cnpj: cpfCnpj,
                    };
                    producerAdd(producer_data);
                }}>
                    Adicionar
                </Button>
            </Form>
        </Card>
    );
}

export default ProducerFormNew;