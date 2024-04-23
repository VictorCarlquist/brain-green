import { Card } from "react-bootstrap";
import { useTotalByTypeAreaQuery } from "../../redux/reducers/api";
import { PieChart } from '@mui/x-charts/PieChart';


function PieByTypeArea() {
  const {data = []} = useTotalByTypeAreaQuery();
  const pieData = data.map(item => ({label: item.areafarm__area_type, value: item.total}));

  return (
    <Card body>
      <h2>Área por Tipo de Solo (ha)</h2>
      <center>
      <PieChart
       series={[
        {
          data: pieData,
        },
        ]}
        width={300}
        height={200}
    />
    </center>
    </Card>
  );
}

export default PieByTypeArea;