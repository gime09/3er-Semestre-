
package paquete2;

public class Clase4 {
    private String atributoPrivate = "atributo privado";

    public Clase4() {
        System.out.println("Constructor privado");
    }
    
    //Creamos un constructor public para crear objetos
    public Clase4(String argumento){ //Aquí se puede llamar al constructor vacio
        this();
        System.out.println("Constructor publico");  
        
    }
    
    //Método private
    private void metodoprivado(){
        System.out.println("Método privado");
        
    }

    public String getAtributoPrivate() {
        return atributoPrivate;
    }

    public void setAtributoPrivate(String atributoPrivate) {
        this.atributoPrivate = atributoPrivate;
    }
    
    
}
