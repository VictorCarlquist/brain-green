import { useState } from 'react';
import { Form, Button, Card } from 'react-bootstrap';
import { useDeleteFarmMutation, useUpdateFarmMutation } from '../../redux/reducers/api';
import { Link } from 'react-router-dom';
import { FarmData } from '../../redux/reducers/api';

function FarmForm(props: {farm: FarmData}) {
    const [saveTxt, setSaveTxt] = useState("Salvar");

    const [farmName, setFarmName] = useState(props.farm.farm_name);
    const [city, setCity] = useState(props.farm.city);
    const [state, setState] = useState(props.farm.state);
    const [totalAreaHectares, setTotalAreaHectares] = useState(props.farm.total_area_hectares);

    const [farmUpdate] = useUpdateFarmMutation();
    const [farmDelete] = useDeleteFarmMutation();

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
                <Form.Control type="number" placeholder="Área Total em Hectares" value={totalAreaHectares} onChange={(e) => setTotalAreaHectares(Number(e.target.value))} />
            </Form.Group>
            <Link to={{ pathname: '/area'  }} state={{farm: props.farm}} >
                <Button variant="secondary">
                    Ver Areas
                </Button>
            </Link>
            <br></br>
            <Button variant="primary" onClick={() => {
                const farm_data = {
                    id: props.farm.id,
                    producer_id: props.farm.producer_id,
                    farm_name: farmName,
                    city: city,
                    state: state,
                    total_area_hectares: totalAreaHectares
                };
                setSaveTxt("Salvando...");
                farmUpdate(farm_data).unwrap().then(() => {
                    setSaveTxt("Salvar");
                });
            }}>
                    {saveTxt}
            </Button>
            <Button variant="danger" onClick={() => {
                farmDelete(props.farm.id);
            }}>
                Deletar
            </Button>
        </Form>
        </Card>
    );
}

export default FarmForm;