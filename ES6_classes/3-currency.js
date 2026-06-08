export default class Currency {
    constructor(code, name) {
        this._code = code;
        this._name = name;
    }

    // code getter and setter
    get code() {
        return this._code;
    }

    set code(value) {
        this._code = value;
    }

    // name getter and setter
    get name() {
        return this._name;
    }

    set name(value) {
        this._name = this.name;
    }

    displayFullCurrency() {
        return `${this.name} (${this._code})`;
    }

}