import { useState } from 'react';
import { Form, Button, Card } from 'react-bootstrap';
import { useAddAreaMutation } from '../../redux/reducers/api';
import { FarmData } from '../../redux/reducers/api';

function AreaFormNew(props: {farm: FarmData}) {
    const [areaType, setAreaType] = useState("");
    const [areaHectares, setAreaHectares] = useState("");
    const [crops, setCrops] = useState("");

    const [areaAdd] = useAddAreaMutation();

    return (
        <Card body>
        <Form>
            <Form.Group controlId="areaType">
                <Form.Label>Tipo de Área</Form.Label>
                <Form.Control type="text" placeholder="Tipo de Área" value={areaType} onChange={(e) => setAreaType(e.target.value)} />
            </Form.Group>

            <Form.Group controlId="areaHectares">
                <Form.Label>Área em Hectares</Form.Label>
                <Form.Control type="number" placeholder="Área em Hectares" value={areaHectares} onChange={(e) => setAreaHectares(e.target.value)} />
            </Form.Group>

            <Form.Group controlId="crops">
                <Form.Label>Culturas</Form.Label>
                <Form.Control type="text" placeholder="Culturas" value={crops} onChange={(e) => setCrops(e.target.value)} />
            </Form.Group>

            <Button variant="primary" onClick={() => {
                const area_data = {
                    farm_id: props.farm.id,
                    area_type: areaType,
                    area_hectares: Number(areaHectares),
                    crops: crops,
                };
                areaAdd(area_data);
            }}>
                Adicionar
            </Button>
        </Form>
        </Card>
    );
}

export default AreaFormNew;