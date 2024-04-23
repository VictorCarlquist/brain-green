import { useState } from 'react';
import { Form, Button, Card } from 'react-bootstrap';
import { useAddAreaMutation } from '../../redux/reducers/api';
import { FarmData } from '../../redux/reducers/api';

function AreaFormNew(props: {farm: FarmData}) {
    const [areaType, setAreaType] = useState("AR");
    const [areaHectares, setAreaHectares] = useState("");
    const [crops, setCrops] = useState("SO");

    const [areaAdd] = useAddAreaMutation();

    return (
        <Card body>
        <Form>
            <Form.Group controlId="areaType">
                <Form.Label>Tipo de Área</Form.Label>
                <Form.Select aria-label="Default select example" value={areaType} onChange={(e) => setAreaType(e.target.value)}>
                    <option value="AR">Agricultável</option>
                    <option value="VE">Vegetação</option>
                </Form.Select>
            </Form.Group>

            <Form.Group controlId="areaHectares">
                <Form.Label>Área em Hectares</Form.Label>
                <Form.Control type="number" placeholder="Área em Hectares" value={areaHectares} onChange={(e) => setAreaHectares(e.target.value)} />
            </Form.Group>

            <Form.Group controlId="crops">
                <Form.Label>Culturas</Form.Label>
                <Form.Select aria-label="Default select example" value={crops} onChange={(e) => setCrops(e.target.value)}>
                    <option value="SO">Soja</option>
                    <option value="MI">Milho</option>
                    <option value="AL">Algodão</option>
                    <option value="CA">Café</option>
                    <option value="CS">Cana de Açucar</option>
                </Form.Select>
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