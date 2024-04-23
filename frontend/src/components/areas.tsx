import { useLocation } from "react-router-dom";
import { useAreaListQuery } from "../redux/reducers/api";
import AreaForm from "./forms/farm_area";
import AreaFormNew from "./forms/farm_area_empty";
import { Col, Container, Row } from "react-bootstrap";


function Areas() {
    const location = useLocation();
    const farm = location.state.farm;
    const {data = []} = useAreaListQuery(farm.id);

    return (
      <Container>
        <Row>
        <Col><h1 className="text-center">Áreas da Fazenda {farm.farm_name}</h1></Col>
        </Row>
        <Row>
          <Col><h3 className="text-center">Total de área: {data.length}</h3></Col>
        </Row>
        <Row>
          <Col>
          <AreaFormNew farm={farm}></AreaFormNew>
          </Col>
        </Row>
        <Row>
        {data.map((area) => (
          <Col md={6}><AreaForm key={area.id} area={area}></AreaForm></Col> 
        ))}
        </Row>

      </Container>
    );
  }

  export default Areas;