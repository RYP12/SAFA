<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
    <xsl:template match="/">
        <html>
            <body>
                <h2>Piratas</h2>

                <br/>

                <table border="1">
                    <tr>
                        <th>Actor</th>
                        <th>Jack Sparrow</th>
                    </tr>
                    <tr>
                        <th>
                            <tr>
                                <th>Nombre completo: </th>
                                <xsl:for-each select="piratas/pirata/datos_actor">
                                    <td>
                                        <xsl:value-of select="nombre"/>
                                    </td>
                                </xsl:for-each>
                            </tr>
                            <tr>
                                <th>Sexo: </th>
                                <xsl:for-each select="piratas/pirata/datos_actor">
                                    <td>
                                        <xsl:value-of select="sexo"/>
                                    </td>
                                </xsl:for-each>
                            </tr>
                            <tr>
                                <th>Fecha nacimiento: </th>
                                <xsl:for-each select="piratas/pirata/datos_actor">
                                    <td>
                                        <xsl:value-of select="nacimiento"/>
                                    </td>
                                </xsl:for-each>
                            </tr>
                        </th>

                        <th>
                        
                        </th>


                    </tr>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>