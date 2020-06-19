from SyntaxAnalyser.parser import parse

text = '''
class Student {
    int age;
    double gpa;

    string first_name;
    string last_name;

    void initialize() {
        age = 18;
        this.gpa = 10.0;
    }

    int getAge() {
        return this.age;
    }

    void setName(string new_name) {
        this.first_name = new_name;
    }

    void report() {
        Print(this.first_name, " ", this.last_name);
        Print("  Age: ", this.age);
    }
}

int main() {
    string s;
    Student t;
    t = new Student;
    t.initialize();

    s = ReadLine();
    t.setName(s);

    return 0;
}
'''
parse(text)
