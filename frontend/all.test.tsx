import renderer from 'react-test-renderer';
import Dashboad from './src/components/dashboard';

it('changes the class when hovered', () => {
  const component = renderer.create(
    <Dashboad></Dashboad>,
  );
  let tree = component.toJSON();
  expect(tree).toMatchSnapshot();

});