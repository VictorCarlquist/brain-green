import { useState } from 'react';
import { Form, Button, Card } from 'react-bootstrap';
import { useDeleteProducerMutation, useUpdateProducerMutation } from '../../redux/reducers/api';
import { Link } from 'react-router-dom';
import { ProducerData } from '../../redux/reducers/api';

function ProducerForm(props: {producer: ProducerData}) {
    const [saveTxt, setSaveTxt] = useState("Salvar");

    const [name, setName] = useState(props.producer.name);
    const [cpfCnpj, setCpfCnpj] = useState(props.producer.cpf_cnpj);

    const [producerUpdate] = useUpdateProducerMutation();
    const [producerDelete] = useDeleteProducerMutation();

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

                <Link to={{ pathname: '/farm'  }} state={{producer: props.producer}} >
                    <Button variant="secondary">
                        Ver Fazendas
                    </Button>
                </Link>

                <Button variant="primary" onClick={() => {
                    const producer_data = {
                        id: props.producer.id,
                        name: name,
                        cpf_cnpj: cpfCnpj,
                    };
                    setSaveTxt("Salvando...");
                    producerUpdate(producer_data).unwrap().then(() => {
                        setSaveTxt("Salvar");
                    });
                }}>
                    {saveTxt}
                </Button>
                <Button variant="danger" onClick={() => {
                    producerDelete(props.producer.id);
                }}>
                    Deletar
                </Button>
            </Form>
        </Card>
    );
}

export default ProducerForm;