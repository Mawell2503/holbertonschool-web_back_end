export default function getNeighborhoodsList() {
    // a variable with a value
    this.sanFranciscoNeighborhoods = ['SOMA', 'Union Square'];
    // an action(method) of a class
    this.addNeighborhood = (newNeighborhood) => {
        this.sanFranciscoNeighborhoods.push(newNeighborhood);
        return this.sanFranciscoNeighborhoods;
    };
}
