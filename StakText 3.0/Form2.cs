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

namespace StakText_3._0
{
    public partial class Form2 : Form
    {
        public Form2()
        {
            InitializeComponent();
            this.MaximizeBox = false;
            this.FormBorderStyle = FormBorderStyle.FixedSingle;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string URL = "https://sakatnex.github.io";
            Process.Start(URL);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string URL = "https://github.com/sakatnex/StakText";
            Process.Start(URL);
        }
    }
}
