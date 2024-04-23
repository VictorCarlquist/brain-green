import { useLocation } from "react-router-dom";
import { useFarmListQuery } from "../redux/reducers/api";
import FarmForm from "./forms/farm";
import FarmFormNew from "./forms/farm_empty";
import { Col, Container, Row } from "react-bootstrap";

function Farms() {
    const location = useLocation();
    const producer = location.state.producer;
    const {data = []} = useFarmListQuery(producer.id);

    return (
      <Container>
        <Row>
        <Col><h1 className="text-center">Fazendas {producer.name}</h1></Col>
        </Row>
        <Row>
          <Col><h3 className="text-center">Total de Fazendas:  {data.length}</h3></Col>
        </Row>
        <Row>
          <Col>
            <FarmFormNew producer={producer}></FarmFormNew>
          </Col>
        </Row>
        <Row>
        {data.map((farm) => (
          <Col md={6}><FarmForm key={farm.id} farm={farm}></FarmForm></Col>
        ))}
        </Row>

      </Container>
    );
  }

  export default Farms;