import { Col, Container, Row } from "react-bootstrap";
import { useProducerlistQuery } from "../redux/reducers/api";
import ProducerForm from "./forms/producer";
import ProducerFormNew from "./forms/producer_empty";

function Producer() {
    const {data = []} = useProducerlistQuery();
    return (
      <Container>
        <Row>
        <Col><h1 className="text-center">Produtores</h1></Col>
        </Row>
        <Row>
          <Col><h3 className="text-center">Total de Produtores: {data.length}</h3></Col>
        </Row>
        <Row>
          <Col>
          <ProducerFormNew></ProducerFormNew>
          </Col>
        </Row>
        <Row>
        {data.map((producer) => (
           <Col md={6}><ProducerForm producer={producer}></ProducerForm></Col>
        ))}
        </Row>


      </Container>
    );
  }

  export default Producer;