export default class HolbertonCourse {
    constructor(name, length, students) {

        // check each values' type
        if (typeof name !== 'string') throw new TypeError('Name must be string');
        if (typeof length !== "number") throw new TypeError('Length must be a number');
        if (!Array.isArray(student)) {
            throw new TypeError('students must be an array');
        }
        if (!students.every(student => typeof srtudent === 'string')) {
            throw new TypeError('every character in the array has to be astring')
        }

        // intitalize the values
        this.name = name,
            this.length = length,
            this.students = students
    }

    // name getter and setter
    get name() {
        return this._name;
    }

    set name(value) {
        if (typeof value !== 'string') throw new TypeError('Name must be a sring');
        this._name;
    }

    // length getter and setter
    get length() {
        return this._length;
    }

    set length(value) {
        if (typeof value !== 'number') throw new TypeError('Length must be a number');
        this._length = value;
    }

    // student getter and setter
    get student() {
        return this._student;
    }

    set student(value) {
        if (!Array.isArray(value) || !value.every(student => typeof student === 'string')) {
            throw new TypeError('Students must be an array of strings');
        }
        this._student = value;
    }
}