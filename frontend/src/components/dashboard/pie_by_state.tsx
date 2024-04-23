import { Card } from "react-bootstrap";
import { useTotalByStateQuery } from "../../redux/reducers/api";
import { PieChart } from '@mui/x-charts/PieChart';


function PieByState() {
  const {data = []} = useTotalByStateQuery();
  const pieData = data.map(item => ({label: item.state, value: item.total}));

  return (
    <Card body>
      <h2>Área por Estado (ha)</h2>
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

export default PieByState;