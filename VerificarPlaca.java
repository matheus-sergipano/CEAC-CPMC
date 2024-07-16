import java.util.Scanner;
import java.util.regex.Pattern;

import javax.swing.JOptionPane;

public class VerificarPlaca {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        long t0 = System.currentTimeMillis();

        while (true) {
            String placa = JOptionPane.showInputDialog("Informe a placa (sem hífen) ou 0 para finalizar: ");
            if (Pattern.matches("^[A-Za-z]{3}[0-9]{4}$", placa)) {
                JOptionPane.showMessageDialog(null, "Segue o padrão de placa antiga. Fazer consulta nas bases de dados para confirmar se é placa veicular.");
            } else if (Pattern.matches("^[A-Za-z]{3}[0-9]{1}[A-Za-z]{1}[0-9]{2}$", placa)) {
                JOptionPane.showMessageDialog(null, "Segue o padrão de placa Mercosul. Fazer consulta nas bases de dados para confirmar se é placa veicular.");
            } else if (placa.equals("0")) {
                JOptionPane.showMessageDialog(null, "Consulta Finalizada.");
                break;
            } else {
                JOptionPane.showMessageDialog(null, "A entrada não é válida!");
            }
        }
        long t1 = System.currentTimeMillis();
        double tempo = ((t1 - t0) / 1000.0);
        JOptionPane.showMessageDialog(null, "Uso finalizado em " + tempo + " segundos");
    }
}
