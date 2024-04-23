import { useState } from 'react';
import { Form, Button, Card } from 'react-bootstrap';
import { useDeleteAreaMutation, useUpdateAreaMutation } from '../../redux/reducers/api';
import { AreaData } from '../../redux/reducers/api';

function AreaForm(props: {area: AreaData}) {
    const [saveTxt, setSaveTxt] = useState("Salvar");

    const [areaType, setAreaType] = useState(props.area.area_type);
    const [areaHectares, setAreaHectares] = useState(props.area.area_hectares);
    const [crops, setCrops] = useState(props.area.crops);

    const [areaUpdate] = useUpdateAreaMutation();
    const [areaDelete] = useDeleteAreaMutation();

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
                <Form.Control type="number" placeholder="Área em Hectares" value={areaHectares} onChange={(e) => setAreaHectares(Number(e.target.value))} />
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
                    id: props.area.id,
                    farm_id: props.area.farm_id,
                    area_type: areaType,
                    area_hectares: areaHectares,
                    crops: crops,
                };
                setSaveTxt("Salvando...");
                areaUpdate(area_data).unwrap().then(() => {
                    setSaveTxt("Salvar");
                });
            }}>
                {saveTxt}
            </Button>
            <Button variant="danger" onClick={() => {
                areaDelete(props.area.id);
            }}>
                Deletar
            </Button>
        </Form>
        </Card>
    );
}

export default AreaForm;