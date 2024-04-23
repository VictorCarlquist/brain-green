import { useState } from 'react';
import { Form, Button, Card } from 'react-bootstrap';
import { useAddFarmMutation } from '../../redux/reducers/api';
import { ProducerData } from '../../redux/reducers/api';

function FarmFormNew(props: {producer: ProducerData}) {
    const [farmName, setFarmName] = useState("");
    const [city, setCity] = useState("");
    const [state, setState] = useState("");
    const [totalAreaHectares, setTotalAreaHectares] = useState("");

    const [farmAdd] = useAddFarmMutation();

    return (
        <Card body>
        <Form>
            <Form.Group controlId="farmName">
                <Form.Label>Nome da Fazenda</Form.Label>
                <Form.Control type="text" placeholder="Nome da Fazenda" value={farmName} onChange={(e) => setFarmName(e.target.value)} />
            </Form.Group>

            <Form.Group controlId="city">
                <Form.Label>Cidade</Form.Label>
                <Form.Control type="text" placeholder="Cidade" value={city} onChange={(e) => setCity(e.target.value)} />
            </Form.Group>

            <Form.Group controlId="state">
                <Form.Label>Estado</Form.Label>
                <Form.Control type="text" placeholder="Estado" value={state} onChange={(e) => setState(e.target.value)} />
            </Form.Group>

            <Form.Group controlId="totalAreaHectares">
                <Form.Label>Área Total em Hectares</Form.Label>
                <Form.Control type="number" placeholder="Área Total em Hectares" value={totalAreaHectares} onChange={(e) => setTotalAreaHectares(e.target.value)} />
            </Form.Group>

            <Button variant="primary" onClick={() => {
                const farm_data = {
                    producer_id: props.producer.id,
                    farm_name: farmName,
                    city: city,
                    state: state,
                    total_area_hectares: Number(totalAreaHectares)
                };
                farmAdd(farm_data);
            }}>
                Adicionar
            </Button>
        </Form>
        </Card>
    );
}

export default FarmFormNew;