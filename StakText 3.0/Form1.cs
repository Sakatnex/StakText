using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
using System.Drawing.Printing;
using System.Drawing.Text;

namespace StakText_3._0
{
    
    
    public partial class Form1 : Form
    {
        private string _openFile;
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void тёмнаяПоУмолчаниюToolStripMenuItem_Click(object sender, EventArgs e)
        {
            richTextBox1.ForeColor = Color.Green;
            richTextBox1.BackColor = Color.Black;
        }

        private void светлаяToolStripMenuItem_Click(object sender, EventArgs e)
        {
            richTextBox1.ForeColor = Color.Black;
            richTextBox1.BackColor = Color.White;
        }

        private void шрифтToolStripMenuItem_Click(object sender, EventArgs e)
        {
            FontDialog myFont = new FontDialog();
            if (myFont.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Font = myFont.Font;
            }
        }

        private void времяИДатаToolStripMenuItem_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += DateTime.Now;
        }

        private void новоеОкноToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Form1 form = new Form1();
            form.Show(this);
        }

        private void открытьToolStripMenuItem_Click(object sender, EventArgs e)
        {
            OpenFileDialog Fdialog = new OpenFileDialog();
            Fdialog.Filter = "Все файлы (*.*) |*.*";
            if (Fdialog.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text = File.ReadAllText(Fdialog.FileName);
                _openFile = Fdialog.FileName;
            }
        }

        private void сохранитьКакToolStripMenuItem_Click(object sender, EventArgs e)
        {
            SaveFileDialog Sdialog = new SaveFileDialog();

            Sdialog.Filter = "Все файлы (*.*) | *.*";
            if (Sdialog.ShowDialog() == DialogResult.OK)
            {
                File.WriteAllText(Sdialog.FileName, richTextBox1.Text);
                _openFile = Sdialog.FileName;
            }
        }

        private void сохранитьToolStripMenuItem_Click(object sender, EventArgs e)
        {
            try
            {
                File.WriteAllText(_openFile, richTextBox1.Text);
            }
            catch (ArgumentException)
            {
                SaveFileDialog Sdialog = new SaveFileDialog();

                Sdialog.Filter = "Текстовики (*.txt) | *.txt";
                if (Sdialog.ShowDialog() == DialogResult.OK)
                {
                    File.WriteAllText(Sdialog.FileName, richTextBox1.Text);
                    _openFile = Sdialog.FileName;
                }
            }
        }

        private void печатьToolStripMenuItem_Click(object sender, EventArgs e)
        {
            PrintDocument pDocument = new PrintDocument();
            pDocument.PrintPage += PrintPageH;
            PrintDialog pDialog = new PrintDialog();
            pDialog.Document = pDocument;
            if (pDialog.ShowDialog() == DialogResult.OK)
            {
                pDialog.Document.Print();
            }
        }

        public void PrintPageH(object sender, PrintPageEventArgs e)
        {
            e.Graphics.DrawString(richTextBox1.Text, richTextBox1.Font, Brushes.Black, 0, 0);
        }

        private void оПрограммеToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Form2 f = new Form2();
            f.ShowDialog();
        }
    }
}
