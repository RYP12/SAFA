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
                            <img src="https://i.pinimg.com/736x/b3/35/72/b33572ca7c8563582a2695272a3065e0.jpg" />
                        </th>

                    </tr>

                    <tr>
                        <th>Películas</th>
                        <th>Roles</th>
                    </tr>

                    <tr>

                        <th>
                            <tr>
                                <th>TITULO</th>
                                <th>SAGA</th>
                            </tr>

                            <tr>
                                <xsl:for-each select="piratas/pirata/peliculas/pelicula/datos">
                                    <td>
                                        <xsl:value-of select="titulo"/>
                                    </td>
                                    <td>
                                        <xsl:value-of select="saga"/>
                                    </td>
                                </xsl:for-each>
                            </tr>
                        </th>

                        <th>

                            <tr>
                                <th>TIPO</th>
                                <th>BARCO</th>
                            </tr>

                            <tr>
                                <xsl:for-each select="piratas/pirata/roles/rol">
                                    <td>
                                        <xsl:value-of select="tipo_rol"/>
                                    </td>
                                    <td>
                                        <xsl:value-of select="barco"/>
                                    </td>
                                </xsl:for-each>
                            </tr>
                        </th>

                    </tr>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>