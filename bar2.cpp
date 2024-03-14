#include <GL/glut.h>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <array> // Include array header for using std::array
using namespace std;

struct FruitData {
    string name;
    int quantity;
};

vector<FruitData> fruitData = {
    {"Avocados", 36},
    {"Oranges", 41},
    {"Bananas", 19},
    {"Kiwi Fruit", 28},
    {"Mangoes", 30},
    {"Grapes", 16}
};

// Defining a type alias for the color array
using Color = array<float, 3>;

// Define a map to store fruit colors
map<string, Color> fruitColors = {
    {"Avocados", {0.0f, 0.5f, 0.0f}},   // slightly dark-green for Avocados
    {"Oranges", {1.0f, 0.5f, 0.0f}},     // Orange for Oranges
    {"Bananas", {1.0f, 1.0f, 0.0f}},     // Yellow for Bananas
    {"Kiwi Fruit", {0.6f, 0.3f, 0.0f}},  // Brown green for Kiwi Fruit
    {"Mangoes", {1.0f, 0.95f, 0.0f}},    // Mango color for Mangoes
    {"Grapes", {0.5f, 0.0f, 0.5f}}       // Purple for Grapes
};

void drawAxes() {
    // Draw horizontal axis
    glColor3f(0.0, 0.0, 0.0);
    glBegin(GL_LINES);
    glVertex2f(0.1, 0.1);//origin
    glVertex2f(0.1, 0.9);//y-max
    glEnd();

    // Draw vertical axis
    glBegin(GL_LINES);
    glVertex2f(0.1, 0.1);//x-min
    glVertex2f(0.9, 0.1); //y-max
    glEnd();

    glColor3f(1.0, 0.0, 0.0 );
    float labelY = 0.1;
    for (int i = 0; i <=55; i+=13){ //y-axis label  
        glRasterPos2f(0.05, labelY);
        string label = to_string(i);
        for (char r:label){
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_10, r);
        }
        labelY += 0.2;
    }

}

void drawBars() {
    float barWidth = 0.08; // width of the bars
    float startX = 0.18;
    float startY = 0.1;
    float maxHeight = 0.8;

    for (size_t i = 0; i < fruitData.size(); ++i) {
        // Get color based on fruit name
        Color color = fruitColors[fruitData[i].name];

        glColor3fv(color.data()); // Set color for the bar
        float barHeight = (float)fruitData[i].quantity / 50.0; // Scale the height of the bars
        glBegin(GL_QUADS);
        glVertex2f(startX + i * 0.10, startY);
        glVertex2f(startX + i * 0.10, startY + barHeight * maxHeight);
        glVertex2f(startX + i * 0.10 + barWidth, startY + barHeight * maxHeight);
        glVertex2f(startX + i * 0.10 + barWidth, startY);
        
        //the 0.10 represents the bar width
        
        glEnd();
    }
}

void drawLabels() { //the labels for the bars for every fruit distro
    float labelX = 0.2;
    float labelY = 0.05;

    for (size_t i = 0; i < fruitData.size(); ++i) {
        glColor3f(0.0, 0.0, 0.0); // Black text
        glRasterPos2f(labelX + i * 0.10, labelY); //
        for (char c : fruitData[i].name) {
            // 
            
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_10, c);
        }
    }
}

void display() {
    glClear(GL_COLOR_BUFFER_BIT);
    drawAxes();
    drawBars();
    drawLabels();
    glFlush();
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(800, 600);
    glutCreateWindow("Fruit Preference Bar Chart");

    glutDisplayFunc(display);
    glClearColor(1.0, 1.0, 1.0, 1.0);
    gluOrtho2D(0.0, 1.0, 0.0, 1.0);
    glutMainLoop();
    return 0;
}
