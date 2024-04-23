import { Col, Container, Row } from "react-bootstrap";
import PieByCrops from "./dashboard/pie_by_crops";
import PieByState from "./dashboard/pie_by_state";
import PieByTypeArea from "./dashboard/pie_by_type_area";
import TotalFarm from "./dashboard/total_farm";
import TotalFarmArea from "./dashboard/total_farm_area";



function Dashboard() {

  return (
    <Container className="text-center">
      <h1>Dashboard</h1>
      <Row>
        <Col>
          <TotalFarm></TotalFarm>
        </Col>
        <Col>
          <TotalFarmArea></TotalFarmArea>
        </Col>
      </Row>
      <Row>
        <Col md={6}>
          <PieByState></PieByState>
        </Col>
        <Col md={6}>
          <PieByCrops></PieByCrops>
        </Col>
        <Col>
          <PieByTypeArea></PieByTypeArea>
        </Col>
      </Row>
    </Container>
  );
}

export default Dashboard;